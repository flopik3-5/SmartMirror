using SmartMirror.Enums;

namespace SmartMirror.Models
{
    public class BluetoothCommand
    {
        public BluetoothCommandType BluetoothCommandType { get; set; }
        public string CommandLine { get; set; }
    }
}