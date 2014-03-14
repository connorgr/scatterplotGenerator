#!/usr/bin/env node
var jsdom = require('/home/connor/scatterplotGenerator/node_modules/jsdom')
, fs = require('fs')

////////////////////////////////////////////////////////////////////////////////////////////////////
// Functions

// The grid version assumes that there is one scatter plot in a given data object
function executeOnJson(data) {
  var colorLayout = data.colorLayout,
      setSize = data.setSize,
      markSize = data.markSize,
      quad = data.quad,
      slope = data.slope,
      repetition = data.repetition;
  runHeadlessBrowser(data, colorLayout+'_'+setSize+'_'+markSize+'_'+slope+'_'+quad+'_'+repetition);
}


function runHeadlessBrowser(gridData, fileName) {
  jsdom.env({features:{QuerySelector:true}, html:htmlStub, src:src, done:function(errors, window) {
    // Function for saving a figure
    function save_fig(selector, file_prefix){
      // Grab the element from the document
      var elem = $(selector)[0];

      // Output if the element exists
      if (elem){
        // Write to file as an SVG
        fs.writeFile(file_prefix + ".svg", elem.outerHTML, write_err);

        // Write to file as a PDF
        // wkhtmltopdf(elem.outerHTML).pipe(fs.creatReadStream(argv.outpre + ".pdf"));
      }
    }
    // Make libraries global loaded in window
    var d3 = window.d3;
    var $  = window.jQuery;

    // Create the scatterplot in the headless browser
    var el = d3.select("scatterplot");
    window.drawScatter(el, gridData);

    // Make sure all SVGs are properly defined
    d3.selectAll("svg").attr("xmlns", "http://www.w3.org/2000/svg");

    // Write the grid to file
    save_fig("svg#plot", argv.outdir + '/' + fileName);
    //save_fig("svg#colorgrid", argv.outdir + name);
  }});
}

// Function to notify user if write fails
function write_err(err){
  if (err){ console.log('Could not output result.' + err); }
}


////////////////////////////////////////////////////////////////////////////////////////////////////
// Main Content

// Validate args
var argv = require('/home/connor/scatterplotGenerator/node_modules/optimist').argv;
if (!( argv.outdir && argv.json )){
    usage  = "Usage: node chartFactory.js --outdir=</path/to/output> --json=</path/to/json>"
    console.log(usage);
    process.exit(1);
}

// Scripts required to make the grids
var scripts = [ "bower_components/jquery/jquery.js",
                "bower_components/d3/d3.js",
                "drawScatter.js"
              ],
    htmlStub = '<!DOCTYPE html><scatterplot></scatterplot>';

var src = scripts.map(function(S){ return fs.readFileSync(S).toString(); })

var data = JSON.parse(fs.readFileSync(argv.json).toString());
executeOnJson(data);
