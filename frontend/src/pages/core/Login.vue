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
                    name="email"
                    label="Логин"
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
                </v-form>
              </v-card-text>
              <v-card-actions class = "d-flex justify-center">
                <v-spacer></v-spacer>
                <v-btn block color="primary" @click="register" :loading="loading">Регистрация</v-btn>
                <v-btn block color="primary" @click="submit_login" :loading="loading">Войти</v-btn>
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
  computed:{
    userId:{
      get(){
        return this.$store.state.user.id
      },
      // set(value){
      //   this.$store.commit("user/storeId", value)
      // }
    },
    userEmail:{
      get(){
        return this.$store.state.user.email
      },
      // set(value){
      //   this.$store.commit("user/storeEmail", value)
      // }
    },
    userPassword:{
      get(){
        return this.$store.state.user.password
      },
      // set(value){
      //   this.$store.commit("user/storePassword", value)
      // }
    }
  },

  data() {
    return {
      loading: false,
      id:0,
      email: '',
      password: '',
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
    async submit_login(user) {
      // let response;
      if(user.id){
        await this.$axios.post('http://localhost:8000/login', user)
      }
        this.$router.push({ name: 'Home' });

      // await this.$store.commit("users/storeData", (await this.$axios.get('http://localhost:8000/')).data)

      // console.log(error.response.data)


      // if (response.status === 200) {
      //   this.$router.push({ name: 'Home' });
      // } else {
      //   console.error('Login failed:', response.data);
      // }
  },
    register() {
      this.$router.push({ name: 'Register' });
    }
  }
}


        // Simulate a successful login response
        // const response = { data: { id: 1, email: 'user@example.com' } };

        // if (user.id) {
        //   // User is in the database, set user data in the store
        //   this.$store.commit("user/storeId", response.data.id);
        //   this.$store.commit("user/storeEmail", response.data.email);
        //   this.$store.commit("user/storePassword", this.password);

        //   // Navigate to the home route
        // } else {
        //   // User not found in the database
        //   this.error = true;
        //   this.result = "Электронная почта или пароль неверны";
        //   this.showResult = true;
        // }



//       if (user.id) {
//         await this.$axios.put("http://localhost:8000" + user.id, user)
//       } 
//       else{
//         await this.$axios.post("http://localhost:8000", user)
//       }

//       await this.resetForm({id:0, email:'', password:''});
//       await this.$store.commit("user/storeData", (await this.$axios.get('http://localhost:8000/')).data);

//     },
//     resetForm(user){
//       this.$store.commit("user/storeId", user.id);
//       // this.$store.commit("user/storeName", user.id);
//       this.$store.commit("user/storeEmail", user.email);
//       this.$store.commit("user/storePassword", user.password);
//     },
//   //     const this = this;

//   //     if (!this.userEmail || !this.password) {
//   //       this.result = "Электронная почта и пароль не должны быть пустыми.";
//   //       this.showResult = true;
//   //       return;
//   //     }

//   //     try {
//   //       const response = await axios.post('http://localhost:8000/login', {
//   //         username: this.userEmail,
//   //         password: this.password
//   //       });

//   //       // If the login is successful, you can handle the response here
//   //       console.log(response.data);
//   //       this.$router.push({ name: 'Home' });

//   //     } catch (error) {
//   //       // If there is an error, handle it here
//   //       console.error('Login failed:', error.response.data);
//   //       this.error = true;
//   //       this.result = "Электронная почта или пароль неверны";
//   //       this.showResult = true;
//   //     }
//   //   },

//     register() {
//       this.$router.push('/register');
//     }
//   }
// }
  // }

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
