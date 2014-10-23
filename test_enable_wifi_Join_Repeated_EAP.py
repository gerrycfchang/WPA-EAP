from gaiatest import GaiaTestCase
import sys,time

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
        
        _wifi_enabled_checkbox_locator = (By.CSS_SELECTOR, '#wifi-enabled input')
        
        checkbox = self.marionette.find_element(*_wifi_enabled_checkbox_locator)
        if not checkbox.is_selected():
            wifiObj.enable_wifi()        
        '''
        import WPA
        wpaObj = WPA.WpaEap(self.marionette)
        wpaObj.enableWifi()
        for x in range(10):
            wpaObj.selectWPANetwork(self.testvars['wifi']['PEAP']['ssid'])
            wpaObj.selectEAPMethod('PEAP')        
            wpaObj.inputIdentity(self.testvars['wifi']['PEAP']['username'])
            wpaObj.inputPassword(self.testvars['wifi']['PEAP']['password'])
            wpaObj.join()                
        
            networkName = wpaObj.getActiveNetworkName()
            
            #v2.0
            #self.assertEqual(networkName, 'TPE_QA')
        
            #v2.1
            self.assertIn(self.testvars['wifi']['PEAP']['ssid'],networkName)

            #forget wifi network
            wpaObj.forgetNetwork(self.testvars['wifi']['PEAP']['ssid'])
        
            time.sleep(3)
        