#include <iostream>

#include "add/add.h"
#include "subtract/subtract.h"

using namespace std;

int main() {
    cout << "5 + 10 = " << add::calc(5, 10) << endl;
    cout << "15 - 10 = " << subtract::calc(15, 10) << endl;
    
    #if defined(BZ_TESTV)
    cout << "BZ_TESTV is defined" << endl;
    #endif

    #if defined(BZ_PROJ_VERSION)
    cout << "Project version: v" << BZ_PROJ_VERSION << endl;
    #endif
    return 0;
}

