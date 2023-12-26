<template>
  <v-card>
    <v-toolbar flat>
      <v-toolbar-title>Реестр</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Поиск"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>

      <v-btn @click="dialog = true">Добавить новый риск</v-btn>
    </v-toolbar>

    <v-data-table
       class="table"
      :headers="headers"
      :items="users"
      :search="search"
      :rows-per-page-items="[5, 10, 20, 50, 100, 200, 1000]">

      
      <template slot="items" slot-scope="props">
        <td>{{ props.item.username }}</td>
        <td>{{ props.item.lastname }}</td>
        <td>{{ props.item.email }}</td>
        <td>{{ props.item.password }}</td>
        <td>{{ props.item.position }}</td>
        <td>
          <v-layout row>
            <v-btn small icon @click="editItem(props.item)"><v-icon>mdi-pencil</v-icon></v-btn>
            <v-btn small icon @click="deleteItem(props.item)"><v-icon>mdi-delete</v-icon></v-btn>
          </v-layout>
        </td>
      </template>
    </v-data-table>

    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
          <v-card-title>
            <span>{{ formTitle }}</span>
          </v-card-title>
            
          <v-card-text>
            <v-text-field v-model="editedItem.username" label="Dessert name"></v-text-field>
            <v-text-field v-model="editedItem.lastname" label="Calories"></v-text-field>
            <v-text-field v-model="editedItem.email" label="Fat (g)"></v-text-field>
            <v-text-field v-model="editedItem.password" label="Carbs (g)"></v-text-field>
            <v-text-field v-model="editedItem.position" label="Protein (g)"></v-text-field>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="close">Отменить</v-btn>
            <v-btn @click="save">Сохранить</v-btn>
          </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
            <v-card-title class="text-xs-title">Вы уверены что хотите удалить данную строку?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Отменить</v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">Удалить</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>
    </v-dialog>
  </v-card>
</template>


<script>
  export default {
    data: () => ({
      search: '',
      dialog: false,
      dialogDelete: false,
      headers: [
          {
            align: 'start',
            value: 'name',
            sortable: true,
            text: 'Dessert (100g serving)',
          },
          { value: 'username', text: 'Username' },
          { value: 'lastname', text: 'Lastname'},
          { value: 'email', text: 'Email' },
          { value: 'password', text: 'Password' },
          { value: 'position', text: 'Job title', sortable: false },

        ],

      desserts: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      defaultItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
    }),

    computed: {
      users() {
        return this.$store.state.users.data;
      },

      formTitle() {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },
    
    async fetch() {
      this.$store.commit(
        "users/storeData", (await this.$axios.get("http://localhost:8000")).data
      )
    },

    watch: {
      dialog(val) {
        val || this.close()
      },
      dialogDelete(val) {
        val || this.closeDelete()
      },
    },

    methods: {
      editItem(item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem(item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm() {
        this.desserts.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close() {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete() {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save() {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
        }
        this.close()
      },
    },
  }
</script>


<style>
  .table {
    border-radius: 3px;
    background-clip: border-box;
    border: 1px solid rgba(0, 0, 0, 0.125);
    box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.21);
    background-color: transparent;
  }

</style> 