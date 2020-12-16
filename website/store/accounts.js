export const state = () => ({
  assets: [],
  liabilities: [],
  account_types: { asset: [], liabilities: [] }
})

export const mutations = {
  add(state, data) {
    // const acc = {
    //   id: data.account.id,
    //   account_type: data.account.type,
    //   name: data.name,
    //   account_name: data.account.name,
    //   balance: data.balance
    // }
    // await this.$axios.post('/accounts', acc)

  },

  clear_account_types(state) {
    state.account_types.asset = []
    state.account_types.liabilities = []
  },
  update_account_types(state, acc) {
    const account = { value: acc, text: acc.name[0].toUpperCase() + acc.name.substr(1).toLowerCase() }

    if (acc.type == 'asset') state.account_types.asset.push(account)
    if (acc.type == 'liability') state.account_types.liabilities.push(account)

  }
  // remove(state, { todo }) {
  //   state.accounts.splice(state.accounts.indexOf(todo), 1)
  // }
}

export const actions = {
  async getAccounts({ commit }) {
    let res = await this.$axios.get('/accounts')
    res.data.accounts.forEach((account) => {
      const parsedAccount = {
        id: account[0].id,
        name: account[0].name,
        account: { name: account[1].name, type: account[1].type },
        balance: account[0].starting_balance
      }
      commit('add', parsedAccount)
    })
  },

  async addAccount({ commit }, data) {
    console.log(data)
    const acc = {
      name: data.name,
      balance: data.balance,
      account_type_id: data.account.id
    }

    await this.$axios.post('/accounts', acc)
  },

  async addAccountType({ commit }, data) {
   await this.$axios.post('/account_type', data)
  },


  async getAccountTypes({ commit }) {
    commit('clear_account_types')
    let account_types = await this.$axios.get('/account_type')
    account_types.data.account_types.forEach((acc_type) => {
      commit('update_account_types', acc_type)
    })
  }
}
