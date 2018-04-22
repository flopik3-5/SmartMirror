using Android.App;
using Android.Content;
using Android.Graphics;
using Android.Media;
using Android.OS;
using Android.Views;
using Android.Widget;
using SmartMirror.Enums;
using SmartMirror.Models;
using Orientation = Android.Widget.Orientation;

namespace SmartMirror.Activities
{
    public class ConfigDialog: DialogFragment
    {
        private ConfigField _field;

        public ConfigDialog(ConfigField field)
        {
            _field = field;
        }

        public override View OnCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState)
        {
            Dialog.SetTitle(_field.Name);
            var view = inflater.Inflate(Resource.Layout.ConfigDialog, null);
            view.FindViewById<LinearLayout>(Resource.Id.configDialogLinearLayout).AddView(GetConfigFieldWidget());
            view.FindViewById<Button>(Resource.Id.configDialogCancelButton).Click += delegate { Dismiss(); };
            return view;
        }

        private View GetConfigFieldWidget()
        {
            View view = null;
            switch (_field.ConfigFieldType)
            {
                case ConfigFieldType.Text:
                    view = new EditText(Context)
                    {
                        Text = _field.Value
                    };
                    break;
                case ConfigFieldType.Time:
                    view = new TimePicker(Context);
                    break;
                case ConfigFieldType.Date:
                    view = new DatePicker(Context);
                    break;
                case ConfigFieldType.Dropdown:
                    view = new RadioGroup(Context);
                    _field.AvailableValues.ForEach(x => ((RadioGroup)view).AddView(new RadioButton(Context)
                    {
                        Text = x
                    }));
                    break;
                case ConfigFieldType.Checkbox:
                    view = new LinearLayout(Context) { Orientation = Orientation.Vertical };
                    _field.AvailableValues.ForEach(x => ((LinearLayout)view).AddView(new CheckBox(Context)
                    {
                        Text = x
                    }));
                    break;
            }
            view?.SetMinimumWidth(int.MaxValue);
            return view;
        }
    }
}