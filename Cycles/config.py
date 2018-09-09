{

	"downloads" : [

		"https://github.com/boberfly/cycles/archive/20180909.tar.gz"

	],

	"license" : "LICENSE",

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -G \"Unix Makefiles\""
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D WITH_CYCLES_STANDALONE_GUI=0"
			" -D WITH_CYCLES_OSL=1"
			#" -D WITH_CYCLES_LOGGING=1"
			" -D WITH_CYCLES_DEBUG=1"
			" -D WITH_CYCLES_OPENSUBDIV=1"
			" -D OPENSUBDIV_ROOT_DIR={buildDir}"
			" -D BOOST_ROOT={buildDir}"
			" -D LLVM_STATIC=1"
			" -D LLVM_ROOT_DIR={buildDir}"
			" -D OPENIMAGEIO_ROOT_DIR={buildDir}"
			" -D OSL_ROOT_DIR={buildDir}"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1"

	],

}
