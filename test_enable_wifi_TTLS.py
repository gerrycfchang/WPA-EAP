from gaiatest import GaiaTestCase
import sys

class TestWpaWlan(GaiaTestCase):       
    
    def setUp(self):
        GaiaTestCase.setUp(self)  
        sys.path.append("./")
        sys.path.append("./tests/functional/WPA-EAP")

    def test_enable_wifi(self):
        '''
        settings = Settings(self.marionette)
        settings.launch()
        wifiObj = settings.open_wifi_settings()
        #v2.0
        #_wifi_enabled_checkbox_locator = (By.CSS_SELECTOR, '#wifi-enabled input')
        _wifi_enabled_checkbox_locator = (By.CSS_SELECTOR, 'li > label > input[type="checkbox"]')
        
        checkbox = self.marionette.find_element(*_wifi_enabled_checkbox_locator)
        if not checkbox.is_selected():
            wifiObj.enable_wifi()
        '''    
        import WPA        
        wpaObj = WPA.WpaEap(self.marionette)
        wpaObj.enableWifi()
        wpaObj.selectWPANetwork(self.testvars['wifi']['TTLS']['ssid'])
        wpaObj.selectEAPMethod('TTLS')
        wpaObj.inputIdentity(self.testvars['wifi']['TTLS']['username'])
        wpaObj.inputPassword(self.testvars['wifi']['TTLS']['password'])
        wpaObj.join()
        
        networkName = wpaObj.getActiveNetworkName()

        #v2.0
        #self.assertEqual(networkName, 'TPE_QA')
        
        #v2.1
        self.assertIn(self.testvars['wifi']['TTLS']['ssid'],networkName)

        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertEqual(networkStatus, 'Connected')
                
        #forget wifi network
        wpaObj.forgetNetwork(self.testvars['wifi']['TTLS']['ssid'])