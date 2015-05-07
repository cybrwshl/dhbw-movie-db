var movieDbApp = angular.module('movieDbApp', ['ngRoute', 'movieDbControllers']);

movieDbApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/movies', {
        templateUrl: 'partials/movie-list.html',
        controller: 'MovieListCtrl',
        activeTab: 'movies',
      }).
      when('/movies/:movieId', {
        templateUrl: 'partials/movie-detail.html',
        controller: 'MovieDetailCtrl',
        activeTab: 'movies',
      }).
      when('/persons', {
        templateUrl: 'partials/person-list.html',
        controller: 'PersonListCtrl',
        activeTab: 'persons',
      }).
      when('/persons/:personId', {
        templateUrl: 'partials/person-detail.html',
        controller: 'PersonDetailCtrl',
        activeTab: 'persons',
      }).
      otherwise({
        redirectTo: '/movies'
      });
  }]);