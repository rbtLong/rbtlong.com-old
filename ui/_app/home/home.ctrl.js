(function() {
    'use strict';

    angular
        .module('app')
        .controller('ctrlHome', ctrlHome);

    function ctrlHome($http) {
        const vm = this;
        vm.skills = {};
        vm.skills.state = 'loading';
        vm.skills.data = [];

        $http({
            method: 'get',
            url: '/api/skills'
        }).then(resp => {
            if(resp.data.hasOwnProperty('success')){
                vm.skills.state = 'normal';
                vm.skills.data = resp.data.content;
            } else {
                vm.skills.state = 'failed';
            }
        }).catch(err => {
            console.log(err);
            vm.skills.state = 'error'
        });

    }

})();