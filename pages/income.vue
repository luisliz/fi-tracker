<template>
  <div>
    <div class="row">
      <div>
        <b-form-datepicker id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
      </div>
      <div>
        <b-form-select v-model="selectedincome" :options="incomes"></b-form-select>
      </div>
      <div>
        <b-form-input placeholder="Amount"></b-form-input>
      </div>
      <div>
        <b-form-select v-model="selectedincometype" :options="incometype"></b-form-select>
      </div>
      <div>
        <b-form-select v-model="selectedaccount" :options="accounts"></b-form-select>
      </div>
      <div>
        <b-button variant="primary">Add</b-button>
      </div>
    </div>

    <b-table hover :items="items" :fields="fields" striped responsive="sm">
      <template #cell(show_details)="row">
        <b-button size="sm" @click="row.toggleDetails" class="mr-2">
          {{ row.detailsShowing ? 'Hide' : 'Show' }} Details
        </b-button>

        <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->
      </template>

      <template #row-details="row">
        <b-card>
          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>Taxes:</b></b-col>
            <b-col>{{ row.item.taxes }}</b-col>
          </b-row>

          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>Saved:</b></b-col>
            <b-col>{{ row.item.savings }}</b-col>
          </b-row>
          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>401k:</b></b-col>
            <b-col>{{ row.item.k401 }}</b-col>
          </b-row>
          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>ROTH IRA:</b></b-col>
            <b-col>{{ row.item.roth }}</b-col>
          </b-row>
          <div class="dropdown-divider"></div>
          <b-row class="mb-2">
            <b-col sm="3" class="text-sm-right"><b>Net Income:</b></b-col>
            <b-col>{{ row.item.net }}</b-col>
          </b-row>
        </b-card>
      </template>
    </b-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedincome: 'job',
      selectedincometype: 'payment',
      incomes: [
        'job',
        'freelancing'
      ],
      selectedaccount: 'Cash',
      accounts: [
        'BPPR',
        'BPPR Sav',
        'TDA',
        'Chase',
        'Cash'
      ],
      incometype: [
        'dividends',
        'payment',
        'bonus',
        'vested shares'
      ],
      fields: ['type', 'source', 'amount', 'account', 'date', 'show_details'],
      items: [
        {
          isActive: false,
          _showDetails: false,
          account: 'Cash',
          type: 'Dividends',
          source: 'VIG',
          amount: '$5802',
          date: '08/05/2020'
        },
        {
          isActive: false,
          _showDetails: false,
          type: 'Payment',
          account: 'BPPR',
          source: 'Bank of America',
          amount: '$5802',
          date: '05/05/2020'
        },
        {
          isActive: false,
          _showDetails: false,
          type: 'Bonus',
          account: 'TDA',
          source: 'MSFT Entry Bonus',
          amount: '$5802',
          date: '05/05/2020'
        },
        {
          isActive: false,
          _showDetails: false,
          type: 'Vested Shares',
          account: 'Vanguard',
          source: 'MSFT',
          amount: '$5802',
          date: '05/05/2020'
        },
      ],
    }
  }
}
</script>
