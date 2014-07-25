from gaiatest import GaiaTestCase
from gaiatest.apps.settings.app import Settings
from marionette.by import By
import sys

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
        wpaObj.selectWPANetwork('Mozilla Mobile')        
        wpaObj.inputPassword('im987tuszyp4v')
        wpaObj.join()                
      
        networkName = wpaObj.getActiveNetworkName()        
        self.assertEqual(networkName, 'Mozilla Mobile')
      
        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertEqual(networkStatus, 'Connected')
        
        method = wpaObj.getStatusSecurityMethod()
        self.assertEqual(method, 'WPA-PSK')
        
        ipAddress = wpaObj.getStatusIP()
        self.assertRegexpMatches(ipAddress, "10.*.*.*") 
        
        signal = wpaObj.getStatusSignalStrengh()
        self.assertNotEqual(signal, "")
        
        speed = wpaObj.getStatusSpeed()
        self.assertNotEqual(speed, "")
                
        #forget wifi network
        wpaObj.forgetNetwork('Mozilla Mobile')