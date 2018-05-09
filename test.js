
function getFunctionName(func) {
    if ( typeof func == 'function' || typeof func == 'object' ) {
        var name = ('' + func).match(/function\s*([\w\$]*)\s*\(/);
    }
    // console.log(name);
    // console.log(name[1]);
    return name && name[1];
}

function printCallStack() {
    var stack = [];
    var fun = arguments.callee;
    do {
        fun = fun.arguments.callee.caller;
        stack.unshift(getFunctionName(fun));
        // console.log(++i + ': ' + fun);
    } while (fun);

    console.log('functions on stack:' + '\n' + stack.join('\n'));
}

function func () {
    printCallStack();
    // for(var i in arguments){
    //     console.log(arguments[i])
    // }
}

function func1 () {
    func()
}

function func2 () {
    func1()
}


function func3 () {
    func2()
}


function func4 () {
    func3()
}

var func5 = function () {
    func4()
}



func5(1,2,3);



