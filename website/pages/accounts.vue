<template>
  <div class="mx-4 my-2">

    <b-row>
      <b-col>
        <b-row>
          <h4>Assets</h4>
        </b-row>
        <b-list-group>
          <Account v-for="asset in accounts.assets"
                   :accType="asset.account.name"
                   :accName="asset.name"
                   :amount="asset.balance" />
        </b-list-group>
      </b-col>
      <b-col>
        <b-row>
          <h4>Liabilities</h4>
        </b-row>
        <b-list-group>
          <Account v-for="liability in accounts.liabilities"
                   acc-is-liability
                   :accType="liability.account.name"
                   :accName="liability.name"
                   :amount="liability.balance" />
        </b-list-group>
      </b-col>
      <b-col class="border-left">
        <h5> Add New Account</h5>
        <div>
          <b-form @submit="onSubmit">
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
      </b-col>

    </b-row>
    <h5>Account Types</h5>
    <b-list-group>
      <b-list-group-item v-for="account in account_types">
        <b-row>
          <b-col>{{ account.name }}</b-col>
          <b-col>{{ account.type }}</b-col>
        </b-row>
      </b-list-group-item>
      <b-list-group-item>
        <b-form inline>
          <b-form-input
            id="input-1"
            type="text"
            v-model="newAccountName"
            placeholder="Enter name"
            required
          ></b-form-input>
          <b-form-radio-group
            id="btn-radios-2"
            v-model="selectedtype"
            :options="acc_types"
            button-variant="outline-primary"
            size="lg"
            name="radio-btn-outline"
            buttons
          ></b-form-radio-group>
          <b-button @click="addAccountType">Add New Account</b-button>
        </b-form>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Account from '~/components/Account.vue'

export default Vue.extend({
  components: { Account },
  methods: {
    async addAccountType() {
      const account_type = {
        name: this.newAccountName,
        type: this.selectedtype
      }
      this.newAccountName = ''
      await this.$axios.post('/account_type', account_type)
      this.getAccountTypes()
    },
    async getAccountTypes() {
      let account_types = await this.$axios.$get('/account_type')
      this.account_types = account_types.account_types
      let assets = []
      let liabilities = []
      account_types.account_types.forEach(acc => {
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
    async onSubmit(event) {
      event.preventDefault()
      const acc = {
        name: this.form.name,
        balance: this.form.balance,
        account_type_id: this.form.account
      }

      await this.$axios.post('/accounts', acc)
      this.getAccounts()
    },

    async getAccounts() {
      let accounts = await this.$axios.get('/accounts')
      this.accounts = accounts.data.accounts
    }

  },
  mounted() {
    this.getAccountTypes()
    this.getAccounts()
  },
  data() {
    return {
      newAccountName: '',
      selectedtype: 'asset',
      acc_types: ['asset', 'liability'],
      account_types: [],
      accounts: { assets: [], liabilities: [] },
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
  }


})
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
