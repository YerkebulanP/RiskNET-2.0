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
                    name="login"
                    label="Логин"
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
                </v-form>
              </v-card-text>
              <v-card-actions class = "d-flex justify-center">
                <v-spacer></v-spacer>
                <v-btn block color="primary" @click="register" :loading="loading">Регистрация</v-btn>
                <v-btn block color="primary" @click="login" :loading="loading">Войти</v-btn>
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
      userEmail: 'admin@railways.kz',
      password: '123456',
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
    login() {
      const vm = this;

      if (!vm.userEmail || !vm.password) {

        vm.result = "Электронная почта и пароль не должны быть пустыми.";
        vm.showResult = true;

        return;
      }

      if (vm.userEmail === vm.$root.userEmail && vm.password === vm.$root.userPassword) {
        vm.$router.push({ name: 'Home' });
      }
      else {
        vm.error = true;
        vm.result = "Электронная почта или пароль неверны";
        vm.showResult = true;
      }
    },
    register(){
        this.$router.push('/register');
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
