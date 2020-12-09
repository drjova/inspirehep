const { gql } = require('apollo-server');

const conferencesSchema = gql`
  type Titles {
    title: String!
  }

  type Adresses {
    cities: [String]
    country: String
    country_code: String
    latitude: Float
    longitude: Float
  }

  type InspireCategories {
    term: String
  }

  type Series {
    name: String
  }

  type ContactDetails {
    email: String
    name: String
  }

  type PublicationInfo {
    artid: String
    journal_issue: String
    journal_title: String
    journal_volume: String
    material: String
    page_start: String
    page_end: String
    pubinfo_freetext: String
    year: Int
  }

  type Proceedings {
    publication_info: PublicationInfo
    source: String
  }

  type Keywords {
    value: String
    control_number: Int!
  }

  type FieldWithStringValue {
    value: String
  }

  type Conference {
    control_number: String!
    titles: [Titles!]
    acronym: [String]
    opening_date: String
    closing_date: String
    adresses: [Adresses]
    cnum: String
    short_description: FieldWithStringValue
    inspire_categories: [InspireCategories]
    series: Series
    contact_details: [ContactDetails]
    proceedings: Proceedings
    public_notes: FieldWithStringValue
    keywords: [FieldWithStringValue]
    urls: [FieldWithStringValue]
    can_edit: Boolean
    deleted: Boolean
  }

  type Query {
    conference(control_number: String): Conference
  }
`;

module.exports = { conferencesSchema: conferencesSchema };
