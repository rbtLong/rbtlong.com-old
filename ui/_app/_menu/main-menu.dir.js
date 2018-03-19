(function() {
    'use strict';

    angular
        .module('app')
        .directive('mainMenu', dirMainMenu);

    function dirMainMenu() {
        return {
            restrict: 'E',
            controller: 'ctrlMainMenu as vm',
            templateUrl: '_app/_menu/main-menu.html'
        }
    }

})();