{

	"downloads" : [

		"https://github.com/OpenImageIO/oiio/archive/Release-1.8.12.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
		 	" cmake"
		 	" -G $CMAKE_GENERATOR"
		 	" -D CMAKE_BUILD_TYPE=$CMAKE_BUILD_TYPE"
		 	" -D CMAKE_INSTALL_PREFIX=$BUILD_DIR"
		 	" -D CMAKE_INSTALL_LIBDIR=$BUILD_DIR/lib"
		 	" -D CMAKE_PREFIX_PATH=$BUILD_DIR"
		 	" -D USE_FFMPEG=NO"
		 	" ..",
		"cd gafferBuild && cmake --build . --config $CMAKE_BUILD_TYPE --target install -- -j $NUM_PROCESSORS"

	],

}
