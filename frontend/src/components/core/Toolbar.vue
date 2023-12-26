<template>
  <v-toolbar
    dark
    app
    :color="$root.themeColor">
    <v-toolbar-title>
      <v-toolbar-side-icon @click="toggleNavigationBar"></v-toolbar-side-icon>
    </v-toolbar-title>
    <v-text-field
      flat
      solo-inverted
      append-icon="search"
      :label="$t('search')">
    </v-text-field>
    <v-spacer></v-spacer>


    <v-dialog
      v-model="dialogSettings"
      width="700">
      <v-card>
        <v-card-title class = "headline" style="justify-content: center;"
          primary-title>
          Настройки
        </v-card-title>

        <v-card-text class="text-xs-center">
            Изменение персональных данных 
         <v-form>
            <v-container>
              <v-layout row wrap>

                <v-flex xs12 xs6 md11>
                  <v-text-field
                    v-model="userEmail"
                    label="Электронный адрес"
                    />
                </v-flex>

                <v-flex xs12 sm6 md11>
                  <v-text-field
                    v-model="password"
                    :append-icon="showPassword ? 'visibility_off' : 'visibility'"
                    :type="showPassword ? 'text' : 'password'"
                    label="Новый пароль"
                    :error="error"
                    @click:append="showPassword = !showPassword" />
                </v-flex>


                <v-flex xs12 sm6 md11>
                  <v-text-field
                    v-model="passwordConfirm"
                    :append-icon="showPasswordConfirm ? 'visibility_off' : 'visibility'"
                    :type="showPasswordConfirm ? 'text' : 'password'"
                    label="Подтвердите пароль"
                    :error="error"
                    @click:append="showPasswordConfirm = !showPasswordConfirm" />
                </v-flex>


              </v-layout>
            </v-container>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="setUpSettings">
            Сохранить изменения
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <v-menu class="toolbar-menu-item" offset-y origin="center center" :nudge-bottom="10" transition="scale-transition">
      <v-btn icon large flat slot="activator" :ripple="false">
        <v-avatar size="42px">
          <img src="https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortFlat&accessoriesType=Sunglasses&hairColor=Black&facialHairType=Blank&clotheType=CollarSweater&clotheColor=Black&eyeType=Default&eyebrowType=Default&mouthType=Smile&skinColor=Light"/>
        </v-avatar>
      </v-btn>
      <v-list>
        <v-list-tile
          v-for="(item,index) in items"
          :key="index"
          :to="!item.href ? { name: item.name } : null"
          :href="item.href"
          ripple="ripple"
          :disabled="item.disabled"
          :target="item.target"
          @click="item.click">
          <v-list-tile-action v-if="item.icon">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-menu>
  </v-toolbar>
</template>
<script>

export default {
  data() {
    return {
      dialog: false,
      dialogSettings: false,
      showPassword: null,
      showPasswordConfirm: null,
      userEmail: null,
      password: null,
      passwordConfirm: null,
      error: false,
      showResult: false,
      result: '',
      items: [
        {
          icon: 'account_circle',
          href: '#',
          title: 'Профиль',
          click: (e) => {
          }
        },
        {
          icon: 'settings',
          href: '#',
          title: 'Настройки',
          click: () => {
            const vm = this;

            vm.dialogSettings = true;
          }
        },
        {
          icon: 'exit_to_app',
          href: '#',
          title: 'Выйти',
          click: () => {
            const vm = this;

            vm.$router.push({ name: 'Login' });
          }
        }
      ],
     
      languages: [
        { name: 'English', languageCode: 'en', path: require('../../assets/flags/en.png') },
      ],
      
  computed: {
    selectedLanguageFlag() {
      const vm = this;

      switch(vm.$i18n.locale) {
        case 'en': return require('../../assets/flags/en.png');
        // case 'ru': return require('../../assets/flags/ru.png');
        // case 'kz': return require('../../assets/flags/kz.png');
        
      }
    }
  },
  methods: {
    toggleNavigationBar() {
      const vm = this;

      vm.$emit('toggleNavigationBar');
    }

    // setUpSettings() {
    //   const vm = this;

    //   if (vm.userEmail === null || vm.password === null || vm.passwordConfirm === null) {

    //     vm.result = "Электронный адрес и пароль не могут быть пустыми.";
    //     vm.showResult = true;

    //     return;
    //   }

    //   if (vm.password !== vm.passwordConfirm) {

    //     vm.error = true;
    //     vm.result = "Пароли не совпадают.";
    //     vm.showResult = true;

    //     return;
    //   }

    //   vm.$root.userEmail = vm.userEmail;
    //   vm.$root.userPassword = vm.password;

    //   vm.result = "Электронный адрес и пароль были изменены";
    //   vm.showResult = true;

    //   vm.dialogSettings = false;
    // },

    // selectLanguage(code) {
    //   const vm = this;

    //   vm.$root.setLanguage(code);
    // }
  }
};
  } }

</script>
<style>
  .toolbar-menu-item {
    padding-left: 5px;
  }

  .selected-language-flag {
    max-width: 45px;
  }

  .language-flag {
    max-width: 40px;
  }


  .languages-list-item {
    cursor: pointer;
    margin-top: -2px;
    margin-left: 1px;
  }

  .languages-list-item-title {
    font-size: 16px;
  }

  .languages-list-item-title:hover {
    color: #41B883;
    font-weight: bold;
  }
  .language-menu {
    border-radius: 25px;
    width: 235px;
    margin-right: 10px;
  }
  
  
</style>