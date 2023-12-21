import Vue from 'vue';
import Router from 'vue-router';

import Home from '../pages/Home.vue';
import Table from '../pages/Table.vue';
import Media from '../pages/Media.vue';
import Snackbar from '../pages/Snackbar.vue';
import Chart from '../pages/Chart.vue';
import Mailbox from '../pages/Mailbox.vue';
import Calendar from '../pages/Calendar.vue';
import Login from '../pages/core/Login.vue';
import Error from '../pages/core/Error.vue';
import Register from '../pages/core/Register.vue';



Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: Home,
    },
    // {
    //   path: '/mailbox',
    //   name: 'Mailbox',
    //   component: Mailbox,
    //   meta: {
    //     breadcrumb: [
    //       { name: 'dashboard', href: 'Dashboard' },
    //       { name: 'mailbox' }
    //     ]
    //   }
    // },
    // {
    //   path: '/snackbar',
    //   name: 'Snackbar',
    //   component: Snackbar,
    //   meta: {
    //     breadcrumb: [
    //       { name: 'dashboard', href: 'Dashboard' },
    //       { name: 'snackbar' }
    //     ]
    //   }
    // },
    // {
    //   path: '/calendar',
    //   name: 'Calendar',
    //   component: Calendar,
    //   meta: {
    //     breadcrumb: [
    //       { name: 'dashboard', href: 'Dashboard' },
    //       { name: 'calendar' }
    //     ]
    //   }
    // },

    {
      path: '/table',
      name: 'Table',
      component: Table,
      meta: {
        breadcrumb: [
          { name: 'Реестр'},
          { name: 'Таблицы' }
        ]
      }
    },
    // {
    //   path: '/media',
    //   name: 'Media',
    //   component: Media,
    //   meta: {
    //     breadcrumb: [
    //       { name: 'dashboard', href: 'Dashboard' },
    //       { name: 'media' }
    //     ]
    //   }
    // },
    {
      path: '/chart',
      name: 'Chart',
      component: Chart,
      meta: {
        breadcrumb: [
          { name: 'Реестр'},
          { name: 'Графики' }
        ]
      }
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
      meta: {
        allowAnonymous: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        allowAnonymous: true
      }
    },
    {
      path: '/error',
      name: 'Error',
      component: Error,
      meta: {
        allowAnonymous: true
      }
    },
  ]
});
