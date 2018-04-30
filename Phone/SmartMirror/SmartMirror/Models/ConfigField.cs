using System.Collections.Generic;
using SmartMirror.Enums;

namespace SmartMirror.Models
{
    public class ConfigField
    {
        public string Name { get; set; }
        public string Value { get; set; }
        public ConfigFieldType ConfigFieldType { get; set; }
        public List<string> AvailableValues { get; set; }
        public List<ConfigField> ConfigFields { get; set; }
    }
}