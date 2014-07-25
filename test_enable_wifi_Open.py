from gaiatest import GaiaTestCase
from gaiatest.apps.settings.app import Settings
from marionette.by import By
import sys,time

class TestWpaWlan(GaiaTestCase):       
    
    def setUp(self):
        GaiaTestCase.setUp(self)
        sys.path.append("./")
        sys.path.append("./tests/functional/WPA-EAP")

    def test_enable_wifi(self):
        settings = Settings(self.marionette)
        settings.launch()
        wifiObj = settings.open_wifi_settings()
        
        _wifi_enabled_checkbox_locator = (By.CSS_SELECTOR, '#wifi-enabled input')
        
        checkbox = self.marionette.find_element(*_wifi_enabled_checkbox_locator)
        if not checkbox.is_selected():
            wifiObj.enable_wifi()        
       
        import WPA
        wpaObj = WPA.WpaEap(self.marionette)
        wpaObj.selectWPANetwork('Mozilla Guest')
        time.sleep(3)                
      
        networkName = wpaObj.getActiveNetworkName()        
        self.assertEqual(networkName, 'Mozilla Guest')
      
        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertEqual(networkStatus, 'Connected')
                
        #forget wifi network
        wpaObj.forgetNetwork('Mozilla Guest')