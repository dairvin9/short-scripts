/*
	To do Application
*/

  var openFile = function(event) {
    var input = event.target;

    var reader = new FileReader();
    reader.onload = function(){
      var dataURL = reader.result;
      var output = document.getElementById('output');
      output.src = dataURL;
    };
    reader.readAsDataURL(input.files[0]);
  };

/*
// global namespace
var MYAPP = MYAPP || {};

// sub namespace
MYAPP.fileIO = {};

var f = evt.target.files[0]; 

    if (f) {
    var r = new FileReader();
      r.onload = function(e) { 
	      var contents = e.target.result;
        alert( "Got the file.n" 
              +"name: " + f.name + "n"
              +"type: " + f.type + "n"
              +"size: " + f.size + " bytesn"
              + "starts with: " + contents.substr(1, contents.indexOf("n"))
        );  
      }
      r.readAsText(f);
    } else { 
      alert("Failed to load file");
    }
  }

  document.getElementById('scheduler.txt').addEventListener('change', readSingleFile, false);

var weekPrompt= "What all is there this week?";
prompt(weekPrompt);

*/