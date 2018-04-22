using System.Collections.Generic;
using Android.App;
using Android.Views;
using Android.Widget;
using SmartMirror.Models;

namespace SmartMirror.Adapters
{
    public class ConfigListAdapter: BaseAdapter<ConfigField>
    {
        private readonly Activity _context;
        private readonly List<ConfigField> _list;

        public ConfigListAdapter(Activity context, List<ConfigField> list)
        {
            _context = context;
            _list = list;
        }

        public override int Count => _list.Count;

        public override long GetItemId(int position)
        {
            return position;
        }

        public override ConfigField this[int position] => _list[position];

        public override View GetView(int position, View convertView, ViewGroup parent)
        {
            var view = convertView ?? _context.LayoutInflater.Inflate(Resource.Layout.ConfigListRow, parent, false);
            view.FindViewById<TextView>(Resource.Id.configListRowName).Text =
                this[position].Name;
            return view;
        }
    }
}