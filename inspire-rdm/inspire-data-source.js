const { RESTDataSource } = require('apollo-datasource-rest');

class ConferenceDataSource extends RESTDataSource {
  constructor() {
    super();
    this.baseURL = 'http://localhost:8000/api/conferences/';
  }

  async getConference(conference_id) {
    const object = await this.get(`${conference_id}`);
    return object.metadata;
  }
}

module.exports = { ConferenceDataSource };
