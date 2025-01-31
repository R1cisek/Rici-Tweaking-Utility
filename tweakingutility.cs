using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace GamingTweaker
{
    public partial class MainForm : Form
    {
        private List<Tweak> tweaks;

        public MainForm()
        {
            InitializeComponent();
            LoadTweaks();
        }

        private void LoadTweaks()
        {
            tweaks = new List<Tweak>
            {
                new Tweak("Disable Fullscreen Optimization", DisableFullscreenOptimization),
                new Tweak("Set High Priority for Games", SetHighPriority),
                // ... přidejte další úpravy zde
            };
        }

        private void ApplyTweaks()
        {
            foreach (var tweak in tweaks)
            {
                tweak.Apply();
            }
            MessageBox.Show("Všechny úpravy byly úspěšně aplikovány!");
        }

        private void DisableFullscreenOptimization()
        {
            // Kód pro zakázání optimalizace na celou obrazovku
        }

        private void SetHighPriority()
        {
            // Kód pro nastavení vysoké priority pro hry
        }

        private void btnApply_Click(object sender, EventArgs e)
        {
            ApplyTweaks();
        }
    }

    public class Tweak
    {
        public string Name { get; }
        public Action Apply { get; }

        public Tweak(string name, Action apply)
        {
            Name = name;
            Apply = apply;
        }
    }
}
