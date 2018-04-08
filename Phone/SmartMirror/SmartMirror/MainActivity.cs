using System;
using System.Collections.Generic;
using Android.App;
using Android.Widget;
using Android.OS;
using Android.Views.Animations;
using SmartMirror.Controllers;

namespace SmartMirror
{
    [Activity(Label = "Smart Mirror", MainLauncher = true, Icon = "@drawable/icon", 
        Theme = "@android:style/Theme.Material.Light.NoActionBar")]
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
            var refreshButton = FindViewById<ImageButton>(Resource.Id.mainRefreshButton);
            refreshButton.Click += RefreshButtonClick;
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

        private void RefreshListDevices(List<string> devices)
        {
            FindViewById<ListView>(Resource.Id.mainDevicesList).Adapter =
                new ArrayAdapter<string>(this, Android.Resource.Layout.SimpleListItem1, devices);
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
    }
}

