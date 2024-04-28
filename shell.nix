with import <nixpkgs> {};
mkShell {
	buildInputs = [python311 nodejs git];
	shellHook = '' 
		export LD_LIBRARY_PATH=$NIX_LD_LIBRARY_PATH;
		source .venv/bin/activate
	'';
}
