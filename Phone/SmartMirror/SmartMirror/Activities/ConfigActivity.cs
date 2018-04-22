using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using Android.App;
using Android.Bluetooth;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Widget;
using Java.IO;
using Newtonsoft.Json;
using SmartMirror.Adapters;
using SmartMirror.Controllers;
using SmartMirror.Enums;
using SmartMirror.Extensions;
using SmartMirror.Models;
using Console = System.Console;

namespace SmartMirror.Activities
{
    [Activity(Label = "Smart Mirror", Icon = "@drawable/icon",
        Theme = "@android:style/Theme.Material.Light")]
    public class ConfigActivity : Activity
    {
        private BluetoothDevice _device;
        private BluetoothSocket _socket;

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            SetContentView(Resource.Layout.Config);

            _device = (BluetoothDevice) Intent.GetParcelableExtra("Device");
            _socket = BluetoothController.GetBluetoothSocket(_device);

            try
            {
                ConnectToSocket(_socket);
            }
            catch (Exception e)
            {
                var intent = new Intent(this, typeof(MainActivity));
                intent.PutExtra("Message", "Unable connect to device");
                SetResult(Result.Canceled, intent);
                Finish();
                return;
            }
            InitializeGui();
        }

        private void ConnectToSocket(BluetoothSocket socket)
        {
            socket.Connect();
            var command = JsonConvert.SerializeObject(new BluetoothCommand
            {
                BluetoothCommandType = BluetoothCommandType.GetConfig
            });
            socket.OutputStream.Write(Encoding.Default.GetBytes(command), 0, command.Length);
            WaitingResponse(socket.InputStream);
        }

        private void WaitingResponse(Stream inputStream)
        {
            var buffer = new List<byte>();
            while (!inputStream.IsDataAvailable()){}
            while (inputStream.IsDataAvailable())
            {
                buffer.Add((byte)inputStream.ReadByte());
            }
            ShowConfig(JsonConvert.DeserializeObject<List<ConfigField>>(Encoding.Default.GetString(buffer.ToArray())));
        }

        private void ShowConfig(List<ConfigField> fields)
        {
            FindViewById<ListView>(Resource.Id.configFieldsList).Adapter = new ConfigListAdapter(this, fields);
        }

        private void InitializeGui()
        {
            FindViewById<TextView>(Resource.Id.configHeaderText).Text = _device.Name ?? _device.Address;
            FindViewById<ListView>(Resource.Id.configFieldsList).ItemClick += ConfigListItemClick;
        }

        private void ConfigListItemClick(object sender, AdapterView.ItemClickEventArgs e)
        {
            new ConfigDialog(e.Parent.GetItemAtPosition(e.Position).Cast<ConfigField>()).Show(
                FragmentManager.BeginTransaction(), "ConfigDialog");
        }
    }
}