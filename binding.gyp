{
  "targets": [
    {
      "target_name": "node-libxslt",
      "sources": [ "src/node_libxslt.cc", "src/stylesheet.cc" ],
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      'dependencies': [
        '<(node_xmljs)/binding.dyp:xmljs-myh',
      	'./deps/libxslt.gyp:libxslt',
      	'./deps/libxslt.gyp:libexslt'
      ]
    }
  ]
}
