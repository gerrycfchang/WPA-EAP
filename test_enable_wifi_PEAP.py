#
from gaiatest import GaiaTestCase
from gaiatest.apps.settings.app import Settings
from marionette.by import By
import sys

class TestWpaWlan(GaiaTestCase):
       
    
    def setUp(self):
        GaiaTestCase.setUp(self)
        sys.path.append("./")       
        #print sys.path 
        

    def test_enable_wifi(self):
        settings = Settings(self.marionette)
        settings.launch()
        wifiObj = settings.open_wifi_settings()
        
        _wifi_enabled_checkbox_locator = (By.CSS_SELECTOR, '#wifi-enabled input')
        
        checkbox = self.marionette.find_element(*_wifi_enabled_checkbox_locator)
        if not checkbox.is_selected():
            wifiObj.enable_wifi()
        
        # select TPE_QA from available networks        
        #this_network_locator = ('xpath', "//li/a[text()='TPE_QA']")
        #preferedNetwork = self.wait_for_element_present(*this_network_locator)
        #preferedNetwork.tap()
        import WPA
        wpaObj = WPA.WpaEap(self.marionette)
        wpaObj.selectWPANetwork('TPE_QA')
        wpaObj.selectEAPMethod('PEAP')
        #wpaObj.choosePhase2Auth('MSCHAP V2')
        wpaObj.inputIdentity('sqa')
        wpaObj.inputPassword('password')
        wpaObj.join()
                
        ''' locate eap first
        _select_eap_locator = (By.CSS_SELECTOR, 'span[class="button icon icon-dialog"]')
        self.wait_for_element_displayed(*_select_eap_locator)
        self.wait_for_element_present(*_select_eap_locator).tap()
        
        
        #switch to frame
        self.marionette.switch_to_frame()
        
        #select PEAP
        options = self.marionette.find_elements(By.CSS_SELECTOR, '#value-selector-container li')
        
        for li in options:
            if li.text == 'PEAP':
                li.tap()
                break
        
        #click OK
        _ok_select_eap = (By.CSS_SELECTOR, 'button.value-option-confirm')
        _ok_button_eap = self.wait_for_element_present(*_ok_select_eap)
        #_ok_button_eap = self.marionette.find_element(*_ok_select_eap)
        _ok_button_eap.tap()
        
        self.apps.switch_to_displayed_app()
        
        #input identity        
        _identity_input_locator = (By.CSS_SELECTOR, '#wifi-auth input[type="text"]')
        identity_field = self.marionette.find_element(*_identity_input_locator)
        identity_field.send_keys('sqa')
        
        #input password        
        _password_input_locator = (By.CSS_SELECTOR, '#wifi-auth input[type="password"]')
        password_field = self.marionette.find_element(*_password_input_locator)
        password_field.send_keys('password')
        
        
        ok_locator = (By.CSS_SELECTOR, 'span[data-l10n-id="ok"]')
        ok_button = self.wait_for_element_present(*ok_locator)
        ok_button.tap()
        
        time.sleep(2)
        '''        
                
        #_connected_message_locator_network = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        #self.wait_for_element_present(*_connected_message_locator_network)
        #_connected_network_name = self.marionette.find_element(*_connected_message_locator_network)
        networkName = wpaObj.getActiveNetworkName()        
        self.assertEqual(networkName, 'TPE_QA')
        
        #_connected_message_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active small')
        #_connected_network_status = self.marionette.find_element(*_connected_message_locator)
        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertEqual(networkStatus, 'Connected')
                
        #forget wifi network
        wpaObj.forgetNetwork('TPE_QA')
