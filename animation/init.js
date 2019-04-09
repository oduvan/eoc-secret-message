//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        var io = new extIO({
            functions: {
                js: 'findMessage',
                python: 'find_message'
            }
        });
        io.start();
    }
);
