<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Account Name:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.name"
          type="text"
          placeholder="Enter name"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="Balance:"
        type="number"
        label-for="input-2"
        description="Only dollar amount will be negative or positive automatically"
      >
        <b-form-input
          id="input-2"
          v-model="form.balance"
          placeholder="Enter balance"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Type:" label-for="input-3">
        <b-form-select
          id="input-3"
          v-model="form.account"
          :options="accountType"
          required
        ></b-form-select>
      </b-form-group>
      <b-button type="submit" variant="outline-success" block>Add</b-button>
    </b-form>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
import { util } from 'prettier'
import isNextLineEmptyAfterIndex = util.isNextLineEmptyAfterIndex

export default Vue.extend({
  mounted() {
    console.log('Loaded side')
    this.getAccountTypes()

  },
  data() {
    return {
      form: {
        balance: null,
        name: '',
        account: null
      },
      assets: [],
      liabilities: [],
      accountType: [],
      show: true
    }
  },

  methods: {
    async getAccountTypes() { //This should be sa
      let account_types = await this.$axios.$get('/account_type')
      console.log(account_types.account_types)
      let assets = []
      let liabilities = []
      account_types.account_types.forEach(acc => {
        console.log(acc)
        if (acc.type == 'asset')
          assets.push({ value: acc.id, text: acc.name[0].toUpperCase() + acc.name.substr(1).toLowerCase() })
        if (acc.type == 'liability')
          liabilities.push({ value: acc.id, text: acc.name[0].toUpperCase() + acc.name.substr(1).toLowerCase() })
      })
      this.accountType = [
        {
          label: 'Assets',
          options: assets
        },
        {
          label: 'Liabilites',
          options: liabilities
        }
      ]
    },
    onSubmit(event) {
      event.preventDefault()
      this.$store.dispatch('accounts/addAccount', this.form)
      this.$store.dispatch('accounts/getAccounts')
      this.$root.$emit('bv::hide::modal', 'modal-1')
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.balance = null
      this.form.name = ''
      this.form.account = null
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
})
</script>
<style>
.nuxtlogo {
  animation: 1s appear;
  margin: auto;
}

@keyframes appear {
  0% {
    opacity: 0;
  }
}
</style>
