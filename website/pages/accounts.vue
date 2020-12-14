<template>
  <b-container>
    <b-col>
      <b-row>
        <h4>Assets</h4>
        <div class="flex-fill"></div>
        <b-button variant="primary" v-b-modal.modal-1>Add</b-button>
      </b-row>
      {{ assets }}
      <b-list-group v-for="asset in assets">
        <Account
          :accType="asset.account.name"
          :accName="asset.name"
          :amount="asset.balance" />
      </b-list-group>
    </b-col>
    <b-col>
      <b-row>
        <h4>Liabilities</h4>
        <div class="flex-fill"></div>
        <b-button variant="primary" v-b-modal.modal-1>Add</b-button>
      </b-row>
      {{ liabilities }}
      <b-list-group v-for="liability in liabilities">
        <Account
          acc-is-liability
          :accType="liability.account.name"
          :accName="liability.name"
          :amount="liability.balance" />
      </b-list-group>
    </b-col>
    <b-modal id="modal-1" hide-footer title="New Account">
      <AddAccount />
    </b-modal>
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Account from '~/components/Account.vue'

export default Vue.extend({
  components: { Account },
  computed: {
    assets() {
      return this.$store.state.accounts.assets
    },
    liabilities() {
      return this.$store.state.accounts.liabilities
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
