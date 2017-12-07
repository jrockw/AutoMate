// background.js

// Called when the user clicks on the browser action.
/*chrome.browserAction.onClicked.addListener(function(tab) {
  // Send a message to the active tab
  /*chrome.tabs.executeScript({
    code: 'var div=document.createElement("div"); document.body.appendChild(div); div.innerText="<button>Fuck Me </button>";'
  });
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
   
  });
});*/

// This block is new!
/*chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "open_new_tab" ) {
      chrome.tabs.create({"url": request.url});
    }
  }
);*/

//chrome.input.ime.onFocus.addListener(function callback)
/*
var ime_api = chrome.input.ime;
var context_id = -1;
console.log("Initializing IME");
ime_api.onFocus.addListener(function(context) {
  console.log('onFocus:' + context.contextID);
  context_id = context.contextID;
});
ime_api.onBlur.addListener(function(contextID) {
  console.log('onBlur:' + contextID);
  context_id = -1;
});
ime_api.onActivate.addListener(function(engineID) {
  console.log('onActivate:' + engineID);
});
ime_api.onDeactivated.addListener(function(engineID) {
  console.log('onDeactivated:' + engineID);
});
ime_api.onKeyEvent.addListener(
function(engineID, keyData) {
  console.log('onKeyEvent:' + keyData.key + " context: " + context_id);
  if (keyData.type == "keydown" && keyData.key.match(/^[a-z]$/)) {
    chrome.input.ime.commitText({"contextID": context_id,
                                 "text": keyData.key.toUpperCase()});
    return true;
  }
  return false
}); */
// button insertion
//chrome.browserAction.onClicked.addListener(function(tab) {
 // chrome.tabs.executeScript(null, {file: "content.js"});
//});







function getCurrentTabUrl(callback) {
  var queryInfo = {
    active: true, 
    currentWindow: true
  };

  chrome.tabs.query(queryInfo, (tabs) => {
    var tab = tabs[0];
    var url = tab.url;
    console.assert(typeof url == 'string', 
      'tab.url should be a string');
    callback(url);
  });
}
