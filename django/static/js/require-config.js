'use strict';
require.config({
    baseUrl: '/static/js',

    paths: {
        googleanalytics: 'google-analytics-tracking',
        mwt: 'MeVisLabWebToolkit',
        jquery: 'jquery/jquery-1.9.1.min',
        jqueryui: 'jqueryui/js/jquery-ui-1.10.1.custom.min',
        jquerycookie: 'jquery.cookie',
        jquerydatatables: 'jquery.dataTables',
        comicwebworkstationwrapper: 'diag/Application/Modules/Macros/COMICWorkstation/web/js/COMICWebWorkstationWrapper'
    },
    shim: {
        jquerycookie: {
            deps: [
                'jquery'
            ]
        },
        jqueryui: {
            deps: [
                'jquery'
            ]
        },
        jquerydatatables: {
            deps: [
                'jquery'
            ]
        },
        comicwebworkstationwrapper: {
            deps: [
                'jquery',
                'mwt'
            ]
        },
    }
});
