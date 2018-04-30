using System;
using System.Collections.Generic;
using System.Text;
using Android.App;
using Android.Bluetooth;
using Android.Content;
using Android.OS;
using Android.Views.Animations;
using Android.Widget;
using Java.Util;
using Newtonsoft.Json;
using SmartMirror.Adapters;
using SmartMirror.Controllers;

namespace SmartMirror.Activities
{
    [Activity(Label = "Smart Mirror", MainLauncher = true, Icon = "@drawable/icon", 
        Theme = "@android:style/Theme.Material.Light")]
    public class MainActivity : Activity
    {
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            
            SetContentView(Resource.Layout.Main);

            InitializeGui();
            InitializeBluetoothController();
        }
        
        private void InitializeGui()
        {
            FindViewById<ImageButton>(Resource.Id.mainRefreshButton).Click += RefreshButtonClick;
            FindViewById<ListView>(Resource.Id.mainDevicesList).ItemClick += DeviceListItemClick;
        }
        
        private void InitializeBluetoothController()
        {
            BluetoothController.DeviceDiscovered += RefreshListDevices;
            BluetoothController.DiscoveryStarted += RefreshButtonDisable;
            BluetoothController.DiscoveryFinished += RefreshButtonEnable;
            BluetoothController.StateChanged += BluetoothStateChanged;
            StartDiscoveryDevices();
        }

        private void RefreshButtonClick(object sender, EventArgs e)
        {
            ((ImageButton) sender).StartAnimation(AnimationUtils.LoadAnimation(this,
                Resource.Animation.refreshButtonTapped));
            StartDiscoveryDevices();
        }

        private void RefreshButtonEnable()
        {
            var refreshButton = FindViewById<ImageButton>(Resource.Id.mainRefreshButton);
            refreshButton.Enabled = true;
            refreshButton.ClearAnimation();
        }

        private void RefreshButtonDisable()
        {
            var refreshButton = FindViewById<ImageButton>(Resource.Id.mainRefreshButton);
            refreshButton.Enabled = false;
            void Handler(object sender, Animation.AnimationEndEventArgs args)
            {
                refreshButton.StartAnimation(AnimationUtils.LoadAnimation(this,
                    Resource.Animation.refreshButtonRotate));
            }
            if (refreshButton.Animation == null)
            {
                Handler(null, null);
            }
            else
            {
               refreshButton.Animation.AnimationEnd += Handler; 
            }
        }

        private void RefreshListDevices(List<BluetoothDevice> devices)
        {
            FindViewById<ListView>(Resource.Id.mainDevicesList).Adapter = new BluetoothListAdapter(this, devices);
        }

        private void DeviceListItemClick(object sender, AdapterView.ItemClickEventArgs e)
        {
            BluetoothController.StopDiscovery();
            var configActivity = new Intent(this, typeof(ConfigActivity));
            configActivity.PutExtra("Device", (BluetoothDevice)e.Parent.GetItemAtPosition(e.Position));
            StartActivityForResult(configActivity, 0);
        }

        private void BluetoothStateChanged(bool isEnable)
        {
            if (isEnable)
            {
                StartDiscoveryDevices();
            }
        }

        private void StartDiscoveryDevices()
        {
            if (BluetoothController.IsEnabled)
            {
                BluetoothController.StartDiscovery();
            }
            else
            {
                BluetoothController.Enable();
            }
        }

        protected override void OnActivityResult(int requestCode, Result resultCode, Intent data)
        {
            base.OnActivityResult(requestCode, resultCode, data);
            
            if (resultCode == Result.Canceled && data != null)
            {
                Toast.MakeText(this, data.GetStringExtra("Message"),ToastLength.Short).Show();
            }
        }
    }
}

