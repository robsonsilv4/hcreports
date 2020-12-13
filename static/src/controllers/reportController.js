(function () {
  'use strict';

  angular
    .module('app')
    .controller(
      'ReportController',
      function ($scope, $rootScope, $http, UserService) {
        $scope.reports = [];
        $scope.showModal = false;
        $scope.reportResponses = [];

        $scope.toggleModal = function (reportResponses) {
          $scope.reportResponses = reportResponses;
          $scope.showModal = !$scope.showModal;
        };

        $scope.init = function (user) {
          var hasUser = typeof user !== 'undefined' && user;
          var url = hasUser ? `/reports/?user_id=${user}` : '/reports/';

          $http.get($rootScope.baseUrl + url).then(function (response) {
            $scope.reports = response.data.results;
          });
        };

        $scope.$watch(
          function () {
            return UserService.getUser();
          },
          function (newUser, oldUser) {
            if (newUser !== oldUser) {
              $scope.init(newUser);
            }
          }
        );

        $scope.init();
      }
    );
})();
