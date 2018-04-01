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
        vm.projects.data = [
            {
                'title': 'Name Pronunciation (Pitzer)',
                'name': 'Name Pronunciation',
                'preview_imgs': ['', '', ''],
                'preview_description':
                    'This project was for Student Commencement preparation to pronounce students names. It is a replacement ' +
                    'for a vendor solution for our school. The projected saved annual cost for the school ' +
                    'while increasing participation seamlessly via the Portal.',
                'tags': ['AngularJs', 'Web Sockets', 'C#', 'MSSQL']
            },
            {
                'title': 'Course Request (Pitzer)',
                'name': 'Course Request',
                'preview_imgs': ['', '', ''],
                'preview_description':
                    'Faculties can use this to request courses, over 1,400 courses are available. Curriculum ' +
                    'Liaisons can lock their department courses, Registrars can review and Administer the course request' +
                    'process. Documents can be audited to see every change in the version of the document and see what ' +
                    'fields changed. Locks report the specific courses that changed and the specific fields that was modified. ' +
                    'This application saved many hours of manual labor and manual process flow.',
                'tags': ['AngularJs', 'Web Sockets', 'C#', 'MSSQL']
            },
            {
                'title': 'Database Helper (Pitzer)',
                'name': 'Database Helper',
                'preview_imgs': ['', '', ''],
                'preview_description':
                    'Eliminated a connection leak issue that plagued the portal for many years. Simplified ' +
                    'database calls using method-chaining and reduced thousands of lines of code.',
                'tags': ['C#', 'Method-Chaining']
            },
            {
                'title': 'Residence Life Housing Assignment (Pitzer)',
                'name': 'Reslife Housing Assignment',
                'preview_imgs': ['', '', ''],
                'preview_description':
                    'Eliminated the need for manual assignment and manual indexing of students to rooms. Our ' +
                    'student body comprises of about 1100 students and 529 possible rooms that can be assigned. ' +
                    'This project has a visual catalog of the rooms and buildings and all students allowing the assignment' +
                    'process to be more automated.',
                'tags': ['Angular 5', 'Web Sockets', 'Go', 'MSSQL', 'Linux', 'Nginx', 'Informix ODBC', 'Active Directory']
            },
            {
                'title': 'Portal X (Pitzer)',
                'name': 'Portal X',
                'preview_imgs': ['', '', ''],
                'preview_description':
                    'An auxiliary portal that supplements our primary portal. It monitors the visitors on the ' +
                    'portal Live using Web Sockets. Errors coming from all application can be tracked via the ' +
                    'auxiliary portal. It also hosts applications such as Residence Life.',
                'tags': ['Angular 5', 'Web Sockets', 'Go', 'MSSQL', 'Linux', 'Nginx', 'Informix ODBC', 'Active Directory']
            }
        ];

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