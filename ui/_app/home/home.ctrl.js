(function() {
    'use strict';

    angular
        .module('app')
        .controller('ctrlHome', ctrlHome);

    function ctrlHome($http) {
        const vm = this;


        // skills section
        vm.skills = {};
        vm.skills.state = 'loading';
        vm.skills.data = [];
        vm.skills.q = '';

        vm.skills.get_comfort_percent = function(skill) {
            try {
                const max = Math.max.apply(Math, vm.skills.data.map(s => s.comfort_level));
                return Math.round((skill.comfort_level / max) * 100);
            } catch(ex) {
                return 0;
            }
        };

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