using System.Collections.Generic;
using Android.App;
using Android.Bluetooth;
using Android.Views;
using Android.Widget;

namespace SmartMirror.Adapters
{
    public class BluetoothListAdapter: BaseAdapter<BluetoothDevice>
    {
        private readonly Activity _context;
        private readonly List<BluetoothDevice> _list;

        public BluetoothListAdapter(Activity context, List<BluetoothDevice> list)
        {
            _context = context;
            _list = list;
        }

        public override int Count => _list.Count;

        public override long GetItemId(int position)
        {
            return position;
        }

        public override BluetoothDevice this[int position] => _list[position];

        public override View GetView(int position, View convertView, ViewGroup parent)
        {
            var view = convertView ?? _context.LayoutInflater.Inflate(Resource.Layout.BluetoothListRow, parent, false);
            view.FindViewById<TextView>(Resource.Id.bluetoothListRowName).Text =
                this[position].Name ?? this[position].Address;
            return view;
        }
    }
}