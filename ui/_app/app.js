(function() {
    'use strict';

    angular.module('app', ['ngRoute', 'ngMaterial', 'ngMessages']);

    angular
        .module('app')
        .config(config);

    function config($routeProvider, $locationProvider) {

        $locationProvider.html5Mode(true);

        $routeProvider
            .when('/', {
                templateUrl: '_app/home/home.html',
                controller: 'ctrlHome as vm'
            });
    }

})();