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
                    v-if="id" 
                    v-model="id"/>

                    <v-text-field
                      append-icon="person"
                      name="username"
                      label="Имя пользователя"
                      type="text"
                      v-model="username"
                      :error="error"
                      :rules="[rules.required]"/>

                    <v-text-field
                      append-icon="person"
                      name="lastname"
                      label="Фамилия"
                      type="text"
                      v-model="lastname"
                      :error="error"
                      :rules="[rules.required]"/>

                    <v-text-field
                      append-icon="person"
                      name="email"
                      label="Корпоративный адрес"
                      type="text"
                      v-model="email"
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

                    <v-select
                        v-model="position"
                        :items="['Главный менеджер', 'Менеджер', 'Директор департамента']"
                        label="Должность"
                        :rules="[rules.required]"
                     ></v-select>

                  </v-form>
                </v-card-text>
                <v-card-actions class = "d-flex justify-center">
                  <v-spacer></v-spacer>
                  <v-btn block color="primary" @click="register ({id, username, lastname, email,password, position})" 
                  :loading="loading"> {{ id ? "Edit" : "Регистрация"}} </v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <!-- <v-snackbar
          v-model="showResult"
          :timeout="2000"
          top>
          {{ result }}
        </v-snackbar> -->
      </v-content>
    </v-app>
  </template>
  
  <script>
  export default {
    computed:{
    userId:{
      get(){
        return this.$store.state.user.id
      },
      set(value){
        this.$store.commit("user/storeId", value)
      }
    },
    userFirstname:{
      get(){
        return this.$store.state.user.username
      },
      set(value){
        this.$store.commit("user/storeUsername", value)
      }
    },
    userLastname:{
      get(){
        return this.$store.state.user.lastname
      },
      set(value){
        this.$store.commit("user/storeLastname", value)
      }
    },
    userEmail:{
      get(){
        return this.$store.state.user.email
      },
      set(value){
        this.$store.commit("user/storeEmail", value)
      }
    },
    userPassword:{
      get(){
        return this.$store.state.user.password
      },
      set(value){
        this.$store.commit("user/storePassword", value)
      }
    },
    userPosition:{
      get(){
        return this.$store.state.user.position
      },
      set(value){
        this.$store.commit("user/storePosition", value)
      }
    }
  },
    data() {
      return {
        loading: false,
        id: 0,
        username:'',
        lastname:'',
        email:'',
        password:'',
        position:'',
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
      async register(user) {
        console.log('$axios instance:', this.$axios); // Log $axios instance

        try {
          let response;
          if (user.id) {
            response = await this.$axios.put('http://localhost:8000/' + user.id, user);
          } else {
            response = await this.$axios.post('http://localhost:8000', user);
          }

          // Handle success
          console.log('User registration successful:', response.data);

          // await this.resetForm({ id: 0, username: '', lastname: '', email: '', password: '', position: '' });
          // await this.$store.commit("users/storeData", (await this.$axios.get('http://localhost:8000/')).data)

          this.$router.push({ name: 'Login' });


        } catch (error) {
          // Handle errors
          console.error('Error during user registration:', error);


        }
      },
      // resetForm(user) {
      //   this.$store.commit('user/storeId', user.id);
      //   this.$store.commit('user/storeUsername', user.username);
      //   this.$store.commit('user/storeLastname', user.lastname);
      //   this.$store.commit('user/storeEmail', user.email);
      //   this.$store.commit('user/storePassword', user.password);
      //   this.$store.commit('user/storePosition', user.position);
      // }      
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

<!-- 
    // methods: {
    //   register() {
    //     const vm = this;
  
    //     if (!vm.userEmail || !vm.password || !vm.userLastname || !vm.userName || !vm.userJobtitle) {
  
    //       vm.result = "Поля не должны быть пустыми";
    //       vm.showResult = true;
  
    //       return;
    //     }
  
    //     else {
    //        vm.$router.push({ name: 'Login' });
    //     }
    //   }
    // }
  -->


  