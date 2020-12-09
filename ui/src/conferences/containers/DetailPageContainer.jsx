import React from 'react';
import { connect } from 'react-redux';
import { useLocation } from 'react-router-dom';
import PropTypes from 'prop-types';
import { Map } from 'immutable';
import { useQuery } from '@apollo/client';
import gql from 'graphql-tag';

import { Row, Col } from 'antd';
import DocumentHead from '../../common/components/DocumentHead';
import ConferenceDates from '../components/ConferenceDates';
import fetchConference from '../../actions/conferences';
import ContentBox from '../../common/components/ContentBox';
import RichDescription from '../../common/components/RichDescription';
import EventSeries from '../../common/components/EventSeries';
import ConferenceContributions from '../components/ConferenceContributions';
import { newSearch } from '../../actions/search';
import { CONFERENCE_CONTRIBUTIONS_NS } from '../../search/constants';
import DeletedAlert from '../../common/components/DeletedAlert';
import { makeCompliantMetaDescription } from '../../common/utils';
import withRouteActionsDispatcher from '../../common/withRouteActionsDispatcher';
import EventTitle from '../../common/components/EventTitle';
import { CONFERENCES_PID_TYPE } from '../../common/constants';

const GET_CONFERENCE = gql`
  query GetConference($control_number: String!) {
    conference(control_number: $control_number) {
      control_number
      acronym
      opening_date
      closing_date
      proceedings {
        publication_info {
          journal_title
        }
      }
      adresses {
        cities
        country
        country_code
        latitude
        longitude
      }
      cnum
      short_description {
        value
      }
      inspire_categories {
        term
      }
      series {
        name
      }
      contact_details {
        email
        name
      }
      proceedings {
        publication_info {
          artid
          journal_issue
          journal_title
          journal_volume
          material
          page_start
          page_end
          pubinfo_freetext
          year
        }
        source
      }
      public_notes {
        value
      }
      keywords {
        value
      }
      urls {
        value
      }
      can_edit
      deleted
      titles {
        title
      }
    }
  }
`;

function DetailPage() {
  const location = useLocation();
  const recid = location.pathname
    .split('/')
    .pop()
    .toString();

  const { data, loading, error } = useQuery(GET_CONFERENCE, {
    variables: { control_number: recid },
    fetchPolicy: 'network-only',
  });

  if (loading) return null;
  if (error) return `Error, ${error}`;

  const { conference } = data;
  const conferenceMap = new Map(Object.entries(conference));

  const controlNumber = conferenceMap.get('control_number');
  const title = conferenceMap.getIn(['titles', 0]);
  const acronym = conferenceMap.getIn(['acronyms', 0]);
  const openingDate = conferenceMap.get('opening_date');
  const closingDate = conferenceMap.get('closing_date');
  const cnum = conferenceMap.get('cnum');
  const description = conferenceMap.getIn(['short_description', 'value']);
  const series = conferenceMap.get('series');
  const deleted = conferenceMap.get('deleted', false);
  const titleMap = title ? new Map(Object.entries(title)) : title;
  const acronymMap = acronym ? new Map(Object.entries(acronym[0])) : acronym;

  const metaDescription = makeCompliantMetaDescription(description);

  return (
    <>
      <DocumentHead
        title={titleMap.get('title')}
        description={metaDescription}
      />
      <Row type="flex" justify="center">
        <Col className="mv3" xs={24} md={22} lg={21} xxl={18}>
          <ContentBox className="sm-pb3">
            <Row>
              <Col span={24}>{deleted && <DeletedAlert />}</Col>
            </Row>
            <Row>
              <Col>
                <h2>
                  <EventTitle title={titleMap} acronym={acronymMap} />
                </h2>
              </Col>
            </Row>
            <Row>
              <Col>
                <ConferenceDates
                  openingDate={openingDate}
                  closingDate={closingDate}
                />
                {cnum && ` (${cnum})`}
              </Col>
            </Row>
            {description && (
              <Row className="mt3">
                <Col>
                  <RichDescription>{description}</RichDescription>
                </Col>
              </Row>
            )}
            {series && (
              <Row className="mt3">
                <Col>
                  <EventSeries series={series} pidType={CONFERENCES_PID_TYPE} />
                </Col>
              </Row>
            )}
          </ContentBox>
        </Col>
      </Row>
      <Row type="flex" justify="center">
        <Col xs={24} md={22} lg={21} xxl={18}>
          <ContentBox>
            <ConferenceContributions conferenceRecordId={controlNumber} />
          </ContentBox>
        </Col>
      </Row>
    </>
  );
}

DetailPage.propTypes = {
  record: PropTypes.instanceOf(Map).isRequired,
};

const mapStateToProps = state => ({
  record: state.conferences.get('data'),
});
const DetailPageContainer = connect(mapStateToProps)(DetailPage);

export default withRouteActionsDispatcher(DetailPageContainer, {
  routeParamSelector: ({ id }) => id,
  routeActions: id => [
    fetchConference(id),
    newSearch(CONFERENCE_CONTRIBUTIONS_NS),
  ],
  loadingStateSelector: state => !state.conferences.hasIn(['data', 'metadata']),
});
