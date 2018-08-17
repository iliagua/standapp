/**
 * setupTests.js
 * Setup test configs for Jest and Enzyme 3+
 * Only for Enzme 3.0 +
 */

// setup file

import { configure } from 'enzyme'
import Adapter from 'enzyme-adapter-react-16'

configure({ adapter: new Adapter() })
