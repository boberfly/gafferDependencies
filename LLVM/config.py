{

	"downloads" : [

		"http://releases.llvm.org/5.0.1/llvm-5.0.1.src.tar.xz",
		"http://releases.llvm.org/5.0.1/cfe-5.0.1.src.tar.xz"

	],

	"license" : "LICENSE.TXT",

	"commands" : [

		"echo $BUILD_DIR",
		"mv ../cfe* tools/clang",
		"mkdir build",
		"cd build &&"
			" cmake"
			" -G $CMAKE_GENERATOR"
			" -D CMAKE_INSTALL_PREFIX=$BUILD_DIR"
			" -D CMAKE_BUILD_TYPE=$CMAKE_BUILD_TYPE"
			" -D LLVM_ENABLE_RTTI=ON"
			" ..",
		"cd build && cmake --build . --config $CMAKE_BUILD_TYPE --target install -- -j $NUM_PROCESSORS"

	],

}
