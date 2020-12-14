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
    <pre>{{form}}</pre>
  </div>
</template>
<script lang="ts">
import { mapMutations } from 'vuex'

export default {
  data() {
    return {
      form: {
        balance: null,
        name: '',
        account: null
      },
      accountType: [
        {
          label: 'Assets',
          options: [
            { value: { name: 'bank', type: 'asset' }, text: 'Bank Account' },
            { value: { name: 'broker', type: 'asset' }, text: 'Broker' },
            { value: { name: 'mortgage', type: 'asset' }, text: 'Mortgage' }
          ]
        },
        {
          label: 'Liabilites',
          options: [
            { value: { name: 'loan', type: 'liability' }, text: 'Loan' },
            { value: { name: 'carLoan', type: 'liability' }, text: 'Car Loan' },
            { value: { name: 'creditCard', type: 'liability' }, text: 'Credit Card' },
            { value: { name: 'studentLoan', type: 'liability' }, text: 'Student Loans' }
          ]
        }
      ],
      show: true
    }
  },

  methods: {
    onSubmit(event) {
      event.preventDefault()
      this.$store.commit('accounts/add', this.form)
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
}
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
