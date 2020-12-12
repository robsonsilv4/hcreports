(function () {
  'use strict';

  angular
    .module('app')
    .controller('UsersController', function ($scope, $rootScope, $http) {
      $http.get(`${$rootScope.baseUrl}/users/`).then(function (response) {
        const users = response.data.results;
        $scope.users = users;
      });

      var currentUser = localStorage.getItem('currentUser');

      if (currentUser) {
        $scope.selectedUser = currentUser;
      }

      $scope.selectUser = function (selectedUser) {
        $scope.selectedUser = selectedUser;
        localStorage.setItem('currentUser', selectedUser);
      };
    });
})();
