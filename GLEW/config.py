{

	"downloads" : [

		"https://downloads.sourceforge.net/project/glew/glew/2.1.0/glew-2.1.0.tgz"

	],

	"license" : "LICENSE.txt",

	"commands" : [

		"mkdir -p {buildDir}/lib64/pkgconfig",
		"make clean && make -j {jobs} install GLEW_DEST={buildDir} LIBDIR={buildDir}/lib",

	],

}
