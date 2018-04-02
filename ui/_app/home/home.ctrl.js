(function() {
    'use strict';

    angular
        .module('app')
        .controller('ctrlHome', ctrlHome);

    function ctrlHome($http) {
        const vm = this;

        // projects section
        vm.projects = {};
        vm.projects.state = 'loading';
        vm.projects.imgs = [];
        vm.projects.data = [];
        vm.projects.get_imgs = function(proj_name) {
            return vm.projects.imgs
                .filter(img => {
                    return img.tags
                        .map(t => t.toLowerCase())
                        .filter(t => t == proj_name.toLowerCase())
                        .length > 0;
                });
        };

        $http({
            method: 'get',
            url: '/api/projects'
        }).then(resp => {
            if(resp.data.hasOwnProperty('success') && resp.data.hasOwnProperty('success')) {
                vm.projects.data = resp.data.content;

                vm.projects.data.forEach(p => {
                    if(p.hasOwnProperty('tags') && p.tags) {
                        try {
                            p.tags = JSON.parse(p.tags);
                        } catch(e) {
                            console.log(`cannot parse project ${p.name}`);
                        }
                    }
                });
            }
        }).catch(err => {
            console.log(err);
        });

        $http({
            method: 'get',
            url: '/api/imgs/projects'
        }).then(resp => {
            if(resp.data.hasOwnProperty('success') && resp.data.hasOwnProperty('success')) {
                vm.projects.imgs = resp.data.content;
                vm.projects.imgs.forEach(img => {
                    try {
                        img.tags = JSON.parse(img.tags);
                    } catch(e) {
                        console.log(`cannot parse img ${p.title}`);
                    }
                })
            }
        }).catch(err => {
            console.log(err);
        });

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