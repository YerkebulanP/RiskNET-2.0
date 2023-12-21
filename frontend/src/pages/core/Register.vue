<template>
    <v-app id="login" class="secondary">
      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4 lg4>
              <v-card class="elevation-1 pa-3">
                <v-card-text>
                  <div class="layout column align-center">
                    <img src="static/ktz_logo.png" width="450" height="120">
                    <!-- <h1 class="flex my-4 primary--text">RiskNET</h1> --><br><br><br><br>
                  </div>
                  <v-form>
                    <v-text-field
                      append-icon="person"
                      name="username"
                      label="Имя пользователя"
                      type="text"
                      v-model="userName"
                      :error="error"
                      :rules="[rules.required]"/>

                    <v-text-field
                      append-icon="person"
                      name="userlastname"
                      label="Фамилия"
                      type="text"
                      v-model="userLastname"
                      :error="error"
                      :rules="[rules.required]"/>

                    <v-text-field
                      append-icon="person"
                      name="userEmail"
                      label="Корпоративный адрес"
                      type="text"
                      v-model="userEmail"
                      :error="error"
                      :rules="[rules.required]"/>    
                      
                    <v-text-field
                      :type="hidePassword ? 'password' : 'text'"
                      :append-icon="hidePassword ? 'visibility_off' : 'visibility'"
                      name="password"
                      label="Пароль"
                      id="password"
                      :rules="[rules.required]"
                      v-model="password"
                      :error="error"
                      @click:append="hidePassword = !hidePassword"/>
                    
                    <v-text-field
                      append-icon="person"
                      name="userJobtitle"
                      label="Должность"
                      type="text"
                      v-model="userJobtitle"
                      :error="error"
                      :rules="[rules.required]"/>                                      
                     
                  </v-form>
                </v-card-text>
                <v-card-actions class = "d-flex justify-center">
                  <v-spacer></v-spacer>
                  <v-btn block color="primary" @click="register" :loading="loading">Регистрация</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <v-snackbar
          v-model="showResult"
          :timeout="2000"
          top>
          {{ result }}
        </v-snackbar>
      </v-content>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        loading: false,
        userName:'',
        userEmail:'admin@railways.kz',
        userLastname:'',
        userJobtitle:'',
        password:'123456',
        hidePassword: true,
        error: false,
        showResult: false,
        result: '',
        rules: {
          required: value => !!value || 'Обязательное поле.'
        }
      }
    },
  
    methods: {
      register() {
        const vm = this;
  
        if (!vm.userEmail || !vm.password || !vm.userLastname || !vm.userName || !vm.userJobtitle) {
  
          vm.result = "Поля не должны быть пустыми";
          vm.showResult = true;
  
          return;
        }
  
        else {
           vm.$router.push({ name: 'Login' });
        }
      }
    }
  }
  </script>
  
  <style scoped lang="css">
    #login {
      height: 50%;
      width: 100%;
      position: absolute;
      top: 0;
      left: 0;
      content: "";
      z-index: 0;
    }
  </style>
  