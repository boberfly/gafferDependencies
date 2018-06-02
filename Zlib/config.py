{

	"downloads" : [

		"https://github.com/madler/zlib/archive/v1.2.11.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"mkdir gafferBuild",

		"cd build &&"
			" cmake"
			" -G $CMAKE_GENERATOR"
			" -D CMAKE_BUILD_TYPE=$CMAKE_BUILD_TYPE"
			" -D CMAKE_INSTALL_PREFIX=$BUILD_DIR"
			" ..",

		"cd gafferBuild && cmake --build . --config $CMAKE_BUILD_TYPE --target install -- -j $NUM_PROCESSORS"

	],

}
