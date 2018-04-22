using System.Collections.Generic;
using System.Linq;
using Android.App;
using Android.Bluetooth;
using Android.Content;
using Java.Util;

namespace SmartMirror.Controllers
{
    [BroadcastReceiver(Enabled = true, Exported = true)]
    [IntentFilter(new []
    {
        BluetoothAdapter.ActionStateChanged,
        BluetoothAdapter.ActionDiscoveryStarted,
        BluetoothAdapter.ActionDiscoveryFinished,
        BluetoothDevice.ActionFound
    })]
    public class BluetoothController: BroadcastReceiver
    {
        private static readonly BluetoothAdapter BluetoothAdapter = BluetoothAdapter.DefaultAdapter;
        private static readonly List<BluetoothDevice> BluetoothDevices = new List<BluetoothDevice>();
        private static readonly UUID Uuid = UUID.FromString("94f39d29-7d6d-437d-973b-fba39e49d4ee");
        
        public delegate void UpdateListDevices(List<BluetoothDevice> devices);
        public static event UpdateListDevices DeviceDiscovered;

        public delegate void DiscoverEvent();
        public static event DiscoverEvent DiscoveryStarted;
        public static event DiscoverEvent DiscoveryFinished;

        public delegate void StateEvent(bool isEnabled);
        public static event StateEvent StateChanged;

        public static bool IsEnabled => BluetoothAdapter.IsEnabled;

        public static void Enable()
        {
            BluetoothAdapter.Enable();
        }

        public static void StartDiscovery()
        {
            BluetoothDevices.Clear();
            if (BluetoothAdapter.IsDiscovering)
            {
                BluetoothAdapter.CancelDiscovery();
            }
            BluetoothAdapter.StartDiscovery();
        }

        public static void StopDiscovery()
        {
            BluetoothAdapter.CancelDiscovery();
        }

        public static BluetoothSocket GetBluetoothSocket(BluetoothDevice device)
        {
            return device.CreateInsecureRfcommSocketToServiceRecord(Uuid);
        }

        public override void OnReceive(Context context, Intent intent)
        {
            switch (intent.Action)
            {
                case BluetoothDevice.ActionFound:
                    OnBluetoothDeviceActionFound(intent);
                    break;
                case BluetoothAdapter.ActionDiscoveryStarted:
                    OnBluetoothAdapterActionDiscoveryStarted();
                    break;
                case BluetoothAdapter.ActionDiscoveryFinished:
                    OnBluetoothAdapterActionDiscoveryFinished();
                    break;
                case BluetoothAdapter.ActionStateChanged:
                    OnActionStateChanged(intent);
                    break;
            }
        }

        private static void OnBluetoothDeviceActionFound(Intent intent)
        {
            var bluetoothDevice = (BluetoothDevice) intent.GetParcelableExtra(BluetoothDevice.ExtraDevice);
            if (!BluetoothDevices.Any(x => x.Address.Equals(bluetoothDevice.Address)))
            {
                BluetoothDevices.Add(bluetoothDevice);
                DeviceDiscovered?.Invoke(BluetoothDevices);
            }
        }

        private static void OnBluetoothAdapterActionDiscoveryStarted()
        {
            DiscoveryStarted?.Invoke();
        }

        private static void OnBluetoothAdapterActionDiscoveryFinished()
        {
            DiscoveryFinished?.Invoke();
        }

        private static void OnActionStateChanged(Intent intent)
        {
            var state = intent.GetIntExtra(BluetoothAdapter.ExtraState, BluetoothAdapter.Error);
            StateChanged?.Invoke(state.Equals((int)State.On));
        }
    }
}